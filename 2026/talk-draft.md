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
    - 
### Classic TDD (2 min)
### Canon TDD (3 min)
### The promise of TDD and where it went sideways (3 min) 
### Alternative approaches, their pros and cons (5 min) 
### Coding and Testing with AI (3 min)
### Have agents use TDD (2 min) 
### Thinking about value (2 min)
### Test level distributions, pyramids and trophies (3 min)
### Shifting to higher level tests (5 min)
### Which test to review (2 min)
### Applying Lean TDD with agents (3 min)

