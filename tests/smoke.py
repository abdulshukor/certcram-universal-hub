"""Optional interactive browser smoke tests. Prerequisite: local server + Playwright Chromium.
Usage: python3 -m http.server 5500  (another terminal: python3 tests/smoke.py)
"""
import os
from playwright.sync_api import sync_playwright

URL=os.environ.get('CERTCRAM_URL','http://127.0.0.1:5500/')

def run():
    with sync_playwright() as p:
        chromium='/usr/bin/chromium' if os.path.exists('/usr/bin/chromium') else None
        browser=p.chromium.launch(headless=True,executable_path=chromium, args=['--no-sandbox'])
        page=browser.new_page(viewport={'width':1280,'height':900})
        errors=[]
        page.on('pageerror', lambda error: errors.append(str(error)))
        page.goto(URL, wait_until='networkidle')
        page.locator('#cert-select option[value="demo"]').wait_for()
        page.locator('#cert-select').select_option('demo')
        page.locator('#cert-name').get_by_text('Interactive Learning Demo').wait_for()
        assert page.locator('#setup-panel').is_visible()
        assert page.locator('#roadmap .sprint').count()==6
        assert page.locator('#cert-select option').count()>=1
        print('PASS: demo loading and six sprints')

        # Sprint title opens guide; marking completion survives page refresh.
        page.locator('[data-action="open-sprint"]').first.click()
        assert page.locator('main h2').inner_text()=='Concept Guide'
        page.locator('[data-action="mark-lesson"]').click()
        assert '1 / 6' in page.locator('#stat-sprints').inner_text()
        page.reload(wait_until='networkidle')
        assert '1 / 6' in page.locator('#stat-sprints').inner_text()
        print('PASS: sprint lesson, mark complete, persistence')

        # Click all main modes and exercise grading.
        page.locator('button[data-tab="blitz"]').click()
        page.locator('.choice').first.click()
        page.locator('button[data-action="submit-answer"]').click()
        assert page.locator('.answer-note').is_visible()
        page.locator('button[data-action="next-question"]').click()
        page.locator('button[data-tab="learn"]').click()
        assert page.locator('#content .tile').count()==6
        page.locator('button[data-tab="quiz"]').click()
        assert page.locator('#quiz-clock').is_visible()
        print('PASS: Exam Blitz, lessons and Full Quiz')

        page.locator('button[data-tab="triggers"]').click()
        assert page.locator('#content .tile').count()==12
        page.locator('#content-search').fill('zzzx-no-match')
        assert page.locator('#content .tile').count()==0
        page.locator('#content-search').fill('')
        assert page.locator('#content .tile').count()==12
        print('PASS: Golden Triggers filters')

        page.locator('button[data-tab="decision"]').click()
        assert page.locator('[data-action="select-tree"]').count()==6
        page.locator('[data-action="tree-choose"]').first.click()
        assert page.locator('[data-action="tree-back"]').is_enabled()
        page.locator('[data-action="tree-choose"]').first.click()
        assert page.locator('.answer-note').count()==1
        page.locator('[data-action="tree-back"]').click()
        page.locator('[data-action="tree-reset"]').click()
        print('PASS: branching decision tree/back/reset')

        page.locator('button[data-tab="speed"]').click()
        assert page.locator('#speed-clock').is_visible()
        page.locator('[data-action="speed-answer"]').first.click()
        assert page.locator('.answer-note').is_visible()
        page.locator('[data-action="speed-next"]').click()
        assert page.locator('#speed-clock').is_visible()
        page.locator('[data-action="speed-reset"]').click()
        print('PASS: speed timer, answer, next, restart')

        page.locator('button[data-tab="trap"]').click()
        assert page.locator('.choice').count()==4
        page.locator('button[data-tab="real-fake"]').click()
        page.locator('[data-action="rf-answer"]').first.click()
        assert page.locator('.answer-note').is_visible()
        page.locator('[data-action="rf-next"]').click()
        print('PASS: Spot the Trap and Real vs Fake')

        page.locator('button[data-tab="battle"]').click()
        assert page.locator('.compare .tile').count()==2
        first=page.locator('.compare .tile h3').first.inner_text()
        page.locator('[data-action="battle-next"]').click()
        assert first!=page.locator('.compare .tile h3').first.inner_text()
        print('PASS: Head-to-Head browse')

        page.locator('button[data-tab="multi"]').click()
        assert page.locator('[data-action="choose-group"]').count()==6
        page.locator('[data-action="choose-group"][data-group="6"]').click()
        assert 'Exam 6' in page.locator('[data-action="choose-group"].active').inner_text()
        page.locator('button.choice').nth(0).click()
        page.locator('button.choice').nth(1).click()
        page.locator('[data-action="submit-answer"]').click()
        assert page.locator('.answer-note').is_visible()
        print('PASS: six Multi-Select groups and answer grading')

        page.locator('button[data-tab="drills"]').click()
        assert page.locator('[data-action="drill-select"]').count()==6
        page.locator('[data-action="drill-move"][data-direction="1"]').first.click()
        page.locator('[data-action="drill-check"]').click()
        assert page.locator('.answer-note').is_visible()
        page.locator('[data-action="drill-reveal"]').click()
        print('PASS: Code & CLI reordering, check/reveal')

        page.locator('button[data-tab="numbers"]').click()
        assert page.locator('#content .tile').count()==8
        page.locator('button[data-tab="rhymes"]').click()
        assert page.locator('#content .tile').count()==10
        page.locator('[data-action="bookmark"]').first.click()
        assert 'Saved' in page.locator('[data-action="bookmark"]').first.inner_text()
        page.reload(wait_until='networkidle')
        page.locator('button[data-tab="rhymes"]').click()
        assert 'Saved' in page.locator('[data-action="bookmark"]').first.inner_text()
        print('PASS: Magic Numbers, ten rhymes, saved bookmarks')

        # Verify copy-to-agent prompt can include requested certification (no automatic generation).
        page.locator('#exam-request').fill('Generic Certification X')
        page.locator('#copy-request').click()
        assert 'Copied!' in page.locator('#toast').inner_text()
        clipboard=page.evaluate('navigator.clipboard.readText()')
        assert 'Generic Certification X' in clipboard
        print('PASS: copy command uses requested certification')

        assert errors==[],f'Unhandled browser errors: {errors}'
        print('PASS: No browser page errors')
        browser.close()

if __name__ == '__main__':
    run()
