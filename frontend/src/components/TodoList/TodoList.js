import React, { useState, useEffect } from 'react';
import axios from 'axios';

function TodoList() {
    console.log("this is todo list")
  // State variable to store todos
  const [todos, setTodos] = useState([]);

  // Function to fetch todos from API
  const fetchTodos = async () => {
    try {
      // Retrieve access token from localStorage
      const accessToken = localStorage.getItem('accessToken');

      // Make a GET request to fetch todos from API with access token in headers
      const response = await axios.get('http://127.0.0.1:8000/api/v1/todo/todos?page=1&page_size=5', {
        headers: {
          'Authorization': `Bearer ${accessToken}`
        }
      });

      // Set todos state with the data received from the API response
      setTodos(response.data);
    } catch (error) {
      // Handle error
      console.error('Error fetching todos:', error);
    }
  };

  // useEffect hook to fetch todos when the component mounts
  useEffect(() => {
    fetchTodos();
  }, []); // Empty dependency array to ensure useEffect runs only once

  return (
    <div>
      <h2>Todo List</h2>
      <ul>
        {/* Map over todos array and render each todo */}
        {todos.map(todo => (
          <li key={todo.id}>{todo.title}</li>
        ))}
      </ul>
    </div>
  );
}

export default TodoList;
