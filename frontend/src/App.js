import React, { useState, useEffect } from 'react';

const UserComponent = () => {
  const [users, setUsers] = useState([]);
  const [restaurants, setRestaurants] = useState([]);
  const [bookmarks, setBookmarks] = useState([]);
  const [bookmarkNum, setBookmarkNum] = useState({ bookmarks: [], restaurant: null });

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
  }, []); 

  useEffect(() => {
    const fetchBookmarks = async () => {
      try {
        const response = await fetch('http://localhost:8000/bookmark');
        const data = await response.json();
        setBookmarks(data);
      } catch (error) {
        console.error('Error fetching bookmarks:', error);
      }
    };

    fetchBookmarks();
  }, []); 

  useEffect(() => {
    const fetchBookmarkNum = async () => {
      try {
        const response = await fetch(`http://localhost:8000/bookmark/8`); // ここを適切な column_id に修正
        const [bookmark, restaurantInfo] = await response.json();
        setBookmarkNum({ bookmarks: bookmark, restaurant: restaurantInfo });
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchBookmarkNum();
  }, []);


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

      <div>
        <h1>Bookmark List    ブックマークデータベースからとってきたやつ！</h1>
        <ul>
          {bookmarks.map(bookmark => (
            <li key={bookmark.column_id}>{bookmark.memo}</li> 
          ))}
        </ul>
      </div>

      <div>
        <h1>Bookmark and Restaurant Information</h1>
        <ul>
          {bookmarkNum.bookmarks && bookmarkNum.bookmarks.map((bookmark, index) => (
            <li key={index}>
              <div>
                <h2>Bookmark</h2>
                <p>Column ID: {bookmark.column_id}</p>
                <p>User ID: {bookmark.user_id}</p>
                <p>Memo: {bookmark.memo}</p>
              </div>
            </li>
          ))}
        </ul>
        <div>
          <h2>Restaurant</h2>
          {bookmarkNum.restaurant && (
            <div>
              <p>Restaurant ID: {bookmarkNum.restaurant.restaurant_id}</p>
              <p>Name: {bookmarkNum.restaurant.name}</p>
              <p>Longitude: {bookmarkNum.restaurant.longitude}</p>
              <p>Latitude: {bookmarkNum.restaurant.latitude}</p>
            </div>
          )}
        </div>
      </div>

    </div>
  );
};

export default UserComponent;
