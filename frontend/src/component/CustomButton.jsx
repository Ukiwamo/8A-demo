import React from 'react';

const CustomButton = ({ children, onClick }) => {
  return (
    <button
      className="bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded transition duration-300"
      onClick={onClick}
    >
      {children}
    </button>
  );
};

export default CustomButton;
