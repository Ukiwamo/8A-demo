import React, { useState, useEffect } from 'react';

const UserComponent = () => {
  const [users, setUsers] = useState([]);
  const [restaurants, setRestaurants] = useState([]);
  const [bookmarks, setBookmarks] = useState([]);
  const [bookmarkNum, setBookmarkNum] = useState(null); // 追加：data_bookmark_num 用の状態変数

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
        const response = await fetch('http://localhost:8000/bookmark/1');
        const data = await response.json();
        setBookmarkNum(data); // 状態変数に設定
      } catch (error) {
        console.error('Error fetching BookmarkNum:', error);
      }
    };

    fetchBookmarkNum(); // 関数の呼び出しを修正
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
  <h1>BookmarkとRestaurantの結び付け練習</h1>
  <ul>
    {bookmarkNum && bookmarkNum.map(num => (
      <li key={num.column_id}>
        <div>
          <span>column id: {num.column_id}</span><br />
          <span>memo content: {num.memo}</span>
        </div>
      </li>
    ))}
  </ul>
</div>
</div>
  );
};

export default UserComponent;
