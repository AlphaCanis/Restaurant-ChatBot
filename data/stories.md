version: "2.0"

stories:

<!-- - story: happy path
  steps:
  - intent: greet
  - action: utter_seats
  - intent: seats
  - action: utter_section
  - action: utter_time -->

<!-- # - story: sad path 1
#   steps:
#   - intent: greet
#   - action: utter_greet
#   - intent: mood_unhappy
#   - action: utter_cheer_up
#   - action: utter_did_that_help
#   - intent: affirm
#   - action: utter_happy

# - story: sad path 2
#   steps:
#   - intent: greet
#   - action: utter_greet
#   - intent: mood_unhappy
#   - action: utter_cheer_up
#   - action: utter_did_that_help
#   - intent: deny
#   - action: utter_goodbye -->
## name path
* greet
  - utter_seats
* seats
  - utter_section
* AC 
  - utter_time
* Non_AC 
  - utter_time  
* time
  - action_time
  
* specials
  - utter_special  
* can_res
  - utter_can_res  
* open
  - utter_open
* timings
  - utter_timings         