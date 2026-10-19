import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const errors = [];
const seenQuestionIDs = new Set();
const readJson = file => JSON.parse(fs.readFileSync(path.join(root, file), 'utf8'));
const registry = readJson('certifications/registry.json');
const required = ['id','code','name','blueprint','domains','sprints','questions','triggers','decisions','battles','drills','numbers','rhymes','realFake'];
const arrays = ['domains','sprints','questions','triggers','decisions','battles','drills','numbers','rhymes','realFake'];
for (const entry of registry.certifications) {
  const pack = readJson(entry.path);
  if (entry.id !== pack.id) errors.push(`${entry.path}: ID does not match registry`);
  for (const key of required) if (pack[key] == null) errors.push(`${pack.id}: missing ${key}`);
  for (const key of arrays) if (!Array.isArray(pack[key]) || !pack[key].length) errors.push(`${pack.id}: missing/nonpopulated ${key}`);
  const domainIDs = new Set(pack.domains.map(d => d.id));
  for (const s of pack.sprints) if (!domainIDs.has(s.domain) || !s.lesson || !s.example || !s.trap) errors.push(`${pack.id}: incomplete lesson: ${s.title}`);
  if (pack.sprints.length !== 6) errors.push(`${pack.id}: expected six study sprints`);
  const qtexts = new Set();
  const multiGroups = new Set();
  let singleCount = 0;
  let multiCount = 0;
  const answerPatterns = new Set();
  for (const q of pack.questions) {
    if (seenQuestionIDs.has(q.id)) errors.push(`duplicate question ID across packs: ${q.id}`);
    seenQuestionIDs.add(q.id);
    if (!domainIDs.has(q.domain)) errors.push(`${q.id}: unknown domain`);
    if (!q.source?.startsWith('https://')) errors.push(`${q.id}: missing official source URL`);
    if (!q.prompt || !q.explanation || q.options.length !== (q.type === 'multi' ? 5 : 4)) errors.push(`${q.id}: missing content or wrong option count`);
    if (!q.correct.length || new Set(q.correct).size !== q.correct.length || q.correct.some(n => !Number.isInteger(n)||n<0||n>=q.options.length)) errors.push(`${q.id}: invalid answer key`);
    if (new Set(q.options.map(x=>x.toLowerCase())).size !== q.options.length) errors.push(`${q.id}: repeated option`);
    if (qtexts.has(q.prompt.toLowerCase())) errors.push(`${q.id}: duplicated question text`);
    qtexts.add(q.prompt.toLowerCase());
    if (q.type === 'multi') { multiCount++;multiGroups.add(q.group);if(q.correct.length<2)errors.push(`${q.id}: not multiple-response`);} else if(q.type==='single'){singleCount++;if(q.correct.length!==1)errors.push(`${q.id}: not single-response`);} else errors.push(`${q.id}: unknown type`);
    answerPatterns.add(q.correct.join(','));
  }
  if (singleCount < 6 || multiCount < 6) errors.push(`${pack.id}: insufficient questions for each mode`);
  if ([1,2,3,4,5,6].some(g => !multiGroups.has(g))) errors.push(`${pack.id}: incomplete Exam 1–6 groups`);
  if (answerPatterns.size < 5) errors.push(`${pack.id}: insufficient answer key variation`);
  for (const [i, t] of pack.decisions.entries()) for (const [j, n] of t.nodes.entries()) if(n.options)for(const o of n.options)if(!t.nodes[o.next])errors.push(`${pack.id} decision ${i}, node ${j}: invalid branch`);
  for (const d of pack.drills) if(d.steps.length!==d.scrambled.length || [...d.scrambled].sort((a,b)=>a-b).some((x,i)=>x!==i))errors.push(`${pack.id}: invalid drill ordering`);
  console.log(`${pack.id}: ${pack.questions.length} questions (${multiCount} multi), ${pack.triggers.length} triggers, ${pack.decisions.length} decision trees, ${pack.drills.length} drills`);
}
if(errors.length){console.error('\nVALIDATION FAILED\n'+errors.join('\n'));process.exitCode=1;}else console.log('PASS: all certification packages meet the structural quality checks.');
