import React, { useState } from 'react';

interface LoginFormProps {
  onSubmit: (email: string, password: string) => void;
}

const LoginForm = ({ onSubmit }: LoginFormProps) => {

  return (
    <div className="login-form">
      <h2>Login</h2>
      <form>
        <div className="form-group">
          <label htmlFor="email">Email:</label>
          <input
            type="email"
            id="email"
            // value={email}
            // onChange={(e) => setEmail(e.target.value)}
            // required
          />
        </div>
        <div className="form-group">
          <label htmlFor="password">Password:</label>
          <input
            type="password"
            id="password"
            // value={password}
            // onChange={(e) => setPassword(e.target.value)}
            // required
          />
        </div>
        <button type="submit" id='login-btn'>Login</button>
        <button type="submit" id='register-btn'>Register</button>

      </form>
    </div>
  );
};

export default LoginForm;