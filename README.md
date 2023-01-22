# UBC-Course-Scheduler
## Description
Our submission to nwHacks 2023! With most of the team members being new to hackathons, we are very excited to present the UBC Course Scheduler. This project is inspired by the process of picking first-year classes before coming here to UBC. As vividly remembered, choosing first ever uni classes are full of thrill and anticipation, but not so much for creating the worklists. Picking and fitting classes into the schedule can be very arduous, and quite frankyl, boring. As such, we've created a way for both upcoming and current UBC students to create many different schedules based on their favourite classes. Don't worry, we are ranking the schedules according to common criteria to give you the best one possible. 

## How it works
- The Scraper
- The Scheduler
  - For those 110 nerds, this is just a giant PSET9. We're generating a (giant!!) search space with all the available sections on ssc. The only constraint is that there should be no conflicting classes. Though, since the search space is too large, we cap the maximum number of timetables to 5000. And for a diversed search space, we frequently "randomize" the combinations of sections.
  - Then, we would score the timetable on the following criteria (based on personal experience):
    - Start-time: classes should not start too early. The ideal time is around 10am.
    - End-time: classes should not end too late. The ideal time is around 4pm.
    - Lunch break: bonus marks for allocating time for lunch (around 11am-1pm)
    - Number of classes in a day: fewer classes in the day equals to less workload which equals to more points
    - Space between classes: the more spaced out the classes are the better the timetable is. But, classes should not be too far (~4 hours) apart.
  - Lastly, we would rank them based on the score and return the top 10 timetables.
- Front End

## Future features
