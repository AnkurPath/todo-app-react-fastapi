import React, { useState } from "react";
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import Login from './components/Login/Login.js';
import TodoList from './components/TodoList/TodoList.js';

function App() {
    // State variable to track the authentication status
    const [isLoggedIn, setIsLoggedIn] = useState(false);

    // Function to handle login process
    const handleLogin = () => {
        // Simulating successful login
        setIsLoggedIn(true);
    };

    return (
        <Router>
            <Routes>
                {/* Route for login page */}
                <Route path="/login" element={<Login onLogin={handleLogin} isLoggedIn={isLoggedIn} />} />

                {/* Route for todo list page */}
                <Route path="/todo" element={isLoggedIn ? <TodoList /> : <Navigate to="/" />} />
            </Routes>
        </Router>
    );
}

export default App;
