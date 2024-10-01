# implement_forgot_password (Issue)

- [ ] Set up the Forgot Password endpoint:

  - [x] Write a failing test for requesting a password reset.
  - [ ] Implement the logic to handle password reset requests.
  - [ ] Make the test pass by validating the password reset request.

- [ ] Generate a Password Reset Token:

  - [ ] Write a failing test for generating a password reset token.
  - [ ] Implement token generation using `itsdangerous` or a similar library.
  - [ ] Make the test pass by generating the token and sending a reset link.

- [ ] Handle Password Reset Submission:

  - [ ] Write a failing test for submitting a new password with the reset token.
  - [ ] Implement the logic to verify the token and update the password.
  - [ ] Make the test pass by allowing password changes only with a valid token.

- [ ] Send a Reset Email:

  - [ ] Write a failing test for sending a reset email.
  - [ ] Implement email sending using a library like `Flask-Mail`.
  - [ ] Make the test pass by sending the reset link to the user’s email.
