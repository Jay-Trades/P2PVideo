import { useState } from 'react'
import './App.css'
import LoginForm from './Components/LoginForm.tsx';

const App = () => {
  const handleLogin = (email: string, password: string) => {
    // Handle the login logic here
    console.log('Login submitted:', { email, password });
  };


  return (
    <>
    <h1>Hello World We back on this grind to get in Google</h1>
      <h1>Vite + React</h1>
      <LoginForm onSubmit={handleLogin} />
    </>
  )
};

export default App;
