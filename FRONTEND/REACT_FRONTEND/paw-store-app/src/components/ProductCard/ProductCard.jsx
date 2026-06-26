import React from 'react';

export const ProductCard = ({ product }) => {
  return (
    <div>
      <h1>{product.nombre}</h1>
      <h2>{product.precio}</h2>
    </div>
  );
};
