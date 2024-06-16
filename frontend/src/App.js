import React, { useState, useEffect } from 'react';

const UserComponent = () => {
  const [users, setUsers] = useState([]);
  const [restaurants, setRestaurants] = useState([]);

  useEffect(() => {
    const fetchUsers = async () => {
      try {
        const response = await fetch('http://localhost:8000/user');
        const data = await response.json();
        setUsers(data);
      } catch (error) {
        console.error('Error fetching users:', error);
      }
    };

    fetchUsers();
  }, []); // [] を渡すことで初回のマウント時のみ実行される


  useEffect(() => {
    const fetchRestaurants = async () => {
      try {
        const response = await fetch('http://localhost:8000/restaurant');
        const data = await response.json();
        setRestaurants(data);
      } catch (error) {
        console.error('Error fetching restaurants:', error);
      }
    };

    fetchRestaurants();
  }, []); // [] を渡すことで初回のマウント時のみ実行される

  return (
    <div>
      <h1>User List    データベースからとってきたやつ！</h1>
      <ul>
        {users.map(user => (
          <li key={user.user_id}>{user.mail}</li>
        ))}
      </ul>

      <div>
      <h1>Restaurant List    データベースからとってきたやつ！</h1>
      <ul>
      {restaurants.map(restaurant => (
            <li key={restaurant.restaurant_id}>{restaurant.name}</li> 
          ))}
      </ul>
    </div>
    </div>

    
  );
};

export default UserComponent;




