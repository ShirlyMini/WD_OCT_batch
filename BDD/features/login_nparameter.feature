Feature: NopCommerce Login to Dashbord

 Scenario Outline: Login and verify Dashbord with valid parameters
   Given : Launch Browser
    When : Open Nopcommerce page
    And : Enter Username "<user>" and Password "<pswd>"
    And : Click Submit
    Then : Presence of Dashboard Logo verified successfully "<status>"

   Examples:
     | user                | pswd     | status |
     | admin@yourstore.com | admin    | True   |
     | admin@yourstore.com | admin123 | False  |
     | abc@yourstore.com   | abc123   | False  |
     | xyz@mystore.com     | mystore  | False  |