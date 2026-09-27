# Is TDD even relevant anymore? Yes, but don't be dumb about it.

## What will attendees learn?

* Why traditional TDD frequently fails to speed us up
* What some alternatives to TDD have been tried
* How to measure the value of different types of tests
* How to tie tests to requirements
* What a good mix of test levels looks like
* How to drive AI development with tests

## Talk Outline 

* Intro to the topic (2 min)
* Who am I (3 min)
* Audience show of hands with TDD and testing practices (2 min)
* Classic TDD (2 min)
* Canon TDD (3 min)
* The promise of TDD and where it went sideways (3 min) 
* Alternative approaches, their pros and cons (5 min) 
* Coding and Testing with AI (3 min)
* Have agents use TDD (2 min) 
* Thinking about value (2 min)
* Test level distributions, pyramids and trophies (3 min)
* Shifting to higher level tests (5 min)
* Which test to review (2 min)
* Applying Lean TDD with agents (3 min)

-----

## Draft & Notes

### Intro to the topic (2 min)

* TDD. Still relevant?
    - Yes but don't be dumb about it
* We're going to cover
    - Why I think coding with tests is faster and easier than without tests
    - Why I think that (some history of my career up to now)
    - Why TDD is more important now than ever before
    - How to do TDD in a sane way
    - And in contrast, how to do TDD in an insane way (according to me)

### Who am I (3 min)

* Lead software engineer in the field of communication test equipment 
* I used to blog a lot at pythontest.com
    - I'd like to do that more. I should.
* Author
    - Python Testing with pytest 
    - Lean TDD 
* Podcast Host
    - Test & Code (2015 - 2025) - 10 years
        - pythontest.com/testandcode
    - Python Bytes (2016 - 2026) - almost 10
        - pythonbytes.fm
    - Python People (2023 - 2024) - not even close to 10
        - but I'm planning on starting up again
        - pythontest.com/pythonpeople
* Went to school for math and art and ended up with a BS and MS in CS
    - that's a lot of S's, and no EE
    - Like really no EE
* Ironically, my lack of EE helped me learn quickly that I needed to communicate well with the domain experts around me to excel at my role.
* Satellite and Component test systems
    - racks 1-4 wide full of instruments and cables and signal switch boxes
    - small team, almost all experts at different stuff
    - not many scheduled meetings
    - we met ad hoc as needed a lot though
    - high cube walls for good sound isolation for focused work
    - close proximity to others when needed
    - access to actual domain expert with customer access and experience
    - we got a lot of stuff right, but testing not so much, no automated tests. 
    - tests were manual, but also by us.  
    - no separate QA team
    - manual testing sucks
    - but we had one release. The code shipped on the computer in the rack.
* Spectrum Analyzer - CDMA cellular measurements
    - These were like the first phones without a huge battery pack
    - I worked closely with the DSP engineer, writing code from the UI and remote interface all the way down to hardware.
    - Lots of automation in our process to speed up coding.
    - For testing, we had separate QA
    - But we naturally coded bones-out or tracer-bullet style, which allowed the QA folks to code up tests while we were developing features
    - Tests lagged implementation by maybe a week at most
    - And a representative was part of our team meetings, along with learning products.
    - And we got a lot of defect reports from people writing docs, which is awesome.
    - It's great to be able to fix a sucky API before it hits the customer.
* Communication Test Box
    - This is like a signal generator with a full communication protocol stack paired with a spectrum analyzer and full receive stack for demodulated signal tests. 
    - Essentially, the box acts a cell tower and full back end, including internet stuff, to test wireless devices.
    - Super fun. Super complex. Lots of people. Lots of teams. Lots of hardware. Lots of code.
    - It was here where I learned about TDD and tried to apply it to my own work.
    - We had a separate QA team here too.
    - But I wanted to make sure my code was working before we sent it off to QA, and I was tired of manually testing my own stuff all the time.
    - Unfortunately, large teams and multiple teams breed inefficiencies.
    - I thought I'd tested my code. Then days or weeks later I get a bug report from QA that finds its way to me. I can't run the test that failed, because I don't have access to their dedicated racks. So I try to either manually reproduce the problem, or better yet, write a small automated snippet to reproduce the problem. And if I can't, then just try a fix and hope it's a fix and ask a test engineer to try it out.
    - I wanted to run those final validation tests myself, and thought it'd have been so much easier to do my work the first time if we had those tests to run during development.
    - I really did think TDD was about that. 
    - The way most people teach it, it's not.
* I took a break and did oscilloscope coding for a while 
    - I introduced the team there to automated test suites during development
* Then back to Comms Testing at R&S
    - Where I am now
    - But here, we didn't have separate QA, the dev team is testing
    - So I was able to decide to do things more efficiently
    - Which is the punchline of the talk
    - And what I call "Lean TDD"
    - We're going to go through this pretty fast, but you can go at your own pace with your own copy. Or better yet, grab a paperback copy and the audio book, read by yours truly.

### Audience show of hands with TDD and testing practices (2 min)

- Who already thinks they know what TDD is? (raise your hand)
- Who's tried it?
- Anyone think it's too much trouble to bother with? 

### Classic TDD (2 min)

- TDD comes from "write the test first" from Extreme Programming
    - One more hand raise thing, who has tried Extreme Programming?
    - Still do it?
    - "test first" quickly became TDD.
- Classic TDD is shorthanded with Red, Green Refactor (diagram)
    * Red - Write a failing test.
    * Green - Write the simplest code possible to make it pass (and all other tests as well).
    * Refactor - Clean up the code.
- The full description in the "by example" book is:
    1. Quickly add a test.
    2. Run all tests and see the new one fail.
    3. Make a little change.
    4. Run all the tests and see them all succeed.
    5. Refactor to remove duplication. 
- But that's not quite all of it.
    - Throughout the book, Kent maintains a list of test cases. 
    - He starts with a brainstormed list, then adds to it along the way.
    - Even though he's implementing test, then code, one test case at a time, that list on the side is guiding what's next and when he's done.
- Even so, it's just the simplistic Red, Green, Refactor that stuck.
    - And that leaves open too many questions

### Canon TDD (3 min)

- In 2023, 21 years after the book, Kent wrote an article describing Canon TDD, with notes that this version is what he meant to teach with the original book.
- Here's a summary
    1. Write a list of test cases you think you need.
    2. Use one item from the list and write a test function for it.
    3. Write or modify code until the test suite, including the new test, all pass.
    4. Optionally refactor the code under test.
    5. During this process, if you think of more needed test cases, add them to the list.
    6. Repeat, starting at step 2, until the list is empty.

- That's longer, and not as catchy, but matches the workflow in the book better than Red/Green/Refactor, and answers a lot of questions.

### The promise of TDD (1 min)

- TDD is and always has been one of the Agile practices. 
- TDD should also be "agile" with a little a.
    - active, light, swift, nimble
    - able to change directions quickly
- Sounds good. Should make us faster, right? 

### Where TDD went sideways (3 min) 

* Separating system tests from unit tests
    - Then
        - GUI testing was annoyingly fiddly with pixel mapping of elements, and cumbersome scripting
    - Now
        - Playwright is way easier, fast, and, well, at least not at the pixel level
        - Although good testable UI design is still a skill
    - APIs, though, have always been awesome
        - They've always been easy to test
        - However, in the 90's, fewer systems had an architecture such that you could test almost all of the system through APIs
* Also there's the QA dept vs development
    - Which isn't helped by really stupid wage disparities in some companies
    - A great test engineer is
        - a great software engineer, plus
        - great communication skills
        - clear writing skills
        - ability to decipher vague speech from all stakeholders
        - ability to lead by example
        - task switch rapidly
        - ...
    - This is a superset of software engineering skills, NOT a subset
        - Some companies get it
    - Let's put a pin in that rant though
* Fixation on fast tests
    - Then
        - developers ran test suites manually
        - if it's slow, they wouldn't do it
    - Now
        - Only tests for the area you're working on needs to be pretty fast
        - The rest can run in CI
        - Still should be fast-ish, but fast is also relative to the project
* Fixation on testing individual functions over APIs
    - This is really where the chaos starts
    - And what slows people down
    - If you don't think so, consider a refactor that shifts a responsibility from one subsystem to another or breaking up a class into two or three in a hierarchy, or any other number of common refactorings. 
    - Any of those wreak havoc on a function level test suite
    - And for an API level test suite? No test changes necessary.

### Alternative approaches, their pros and cons (5 min) 

- London or Mockist
    - it just seems like so much work
    - and it seems like testing implementation, not behavior
    - and I find the tests hard to read
- Behavior driven development, BDD
    - Behaviors, yay! Gherkin, boo!
    - But it did pull in acceptance criteria for the system
        - which is awesome
- Acceptance Test Driven Development, ATDD
    - This can be very close to BDD, or close to Lean TDD, depending on your interpretations.
    - I choose to interpret it as Lean TDD
    - However, ATDD really has nothing to say about how to build subsystems and smaller units, which is a shame.
- Lean TDD
    - a.k.a "Unified Field Theory for TDD"
    - ATDD at the top, some subsystem testing as needed, one test suite if possible
    - Room for developers and test engineers
    - Don't be wasteful
    - Ceremony as necessary
    - And the testing trophy, that rocks!
    - Essentially, test at the highest level that's reasonable
        - This minimizes rework when refactoring
        - Thus encouraging refactoring and second drafts
        - Stop shipping your first draft!
        - It's a terrible practice for blog posts, homework assignments, and is never done for books, so why do it with software.
    - Minimize overlap of testing at different levels
    - Make sure everyone can run every test in the system
    - Locally if possible
        - We have complex hardware, so we have a shared pool of instruments. You can find one matching the scenario in a bug report, reserve it for a bit, run a test locally, debug it, grab logs, whatever. 
        - Saves so much time in the back and forth between test reporter and developer. 
            - How did you set it up now? 
            - How do I run the test?
            - Ok. I think I've fixed it, can you try it again on version x.y.z?
            - Can you turn on some specific logging with command BLAH and rerun the test?
        - That's such a waste. Just let the developer run the test and do whatever they want.  

### Coding and Testing with AI (3 min)

- There's a level where you want to make sure the code is doing what it's supposed to do
    - Have "what it's supposed to do" be encoded as tests.
    - Either write these tests yourself or at least review them.
- At the very least, you should care what the system does
    - So write or review tests at those levels
- At the level of your part of the system that you are responsible for
    - Either write these tests yourself or at least review them.
- At whatever level you're willing to have an AI write code such that you're not going to review the code, decide whether or not you need to review the tests for that level
    - You can make that decision if you trust the tests at higher levels
- Keeping fixed "do not modify" tests at higher levels allows AI, agents, subcontractors, interns, whoever to have the freedom to implement their part however they want.
    - You can still review, but guardrails of system tests are nice

### Have agents use TDD (2 min) 

- Having agents work on tasks, with a rough outline spec
    - need to try with and without directing them to write their own tests and use TDD 
- But I do know that directing them to run a specific set of tests as part of the process is very useful
    - I don't have to keep trying it manually
    - Same experience as QA and dev
    - Except this time, I'm QA
- Even if I direct an AI to write the high level tests, I'll review those to make sure they conform to my understanding of "this works", and the agent can keep running them as it debugs and fixes stuff.
    - this is the equivalent of letting developers run tests that have been developed by QA

### Value and test distributions

- Value & Waste
- In Lean, waste is anything that doesn't directly add value to a customer.
- We can't eliminate waste. There is some effort that provides value to the development team or management team but not directly to customers, and tests are one of those things.
- Yes, throw your tomatoes now. Tests are waste, in a lean sense.
- So we want to minimize tests while maximizing value.
- I think the best way to do that is to follow a modified test trophy
- The idea came from Kent C. Dodds, but I've changed the names
- (show a pic of the modified trophy from the book)
- discuss layers and where the value lies

### Shifting to higher level tests (5 min)

- How is Lean TDD "Unified TDD Theory"?
- It just makes value sense to think of the testing stack as one thing.
- To not have redundant tests at multiple levels
- To test at the highest level possible to maximize zero-test-rework refactoring potential.

### Being honest about test value

- Maybe you love your unit tests
- That's fine
- But I ask you, if you have two example tests, one that represents a customer requirement as an acceptance criteria, and one that's a unit test representing something that some developer thought was important at some time.
- If you are confident that the system level acceptance tests are thorough and represent the teams understanding of what's needed to ship.
- And if you have one failing test in the system, would you rather have that failing test a unit test that's hard to track back to system requirements?
- Or would you rather have the system test directly tied to a customer requirement fail?
- I know the answer for me. 
- I'd rather have all system tests directly tied to customer requirements pass.
- I'd still investigate the unit test failure.
- But honestly, I've even written my own small level tests that are more stringent than the real system requirements for my component.
- And that's why I can confidently say that system tests directly tied to requirements are way more valuable.
- Just something to think about

### RTFM

For a longer discussion do please check out the book.
It's only 100 pages, and the audio book is short also, especially at 1.2 to 1.5x speed.
And please listen to Python People when it reboots.


