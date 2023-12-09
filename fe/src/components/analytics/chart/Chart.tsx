import React from 'react';
import styled from 'styled-components';

interface IImgData {
  image_file: string;
  value: string;
}

const Img = styled.img`
  width: 700px;
  height: 400px;
`;

function Chart({ image_file, value }: IImgData) {
  const IMG_URL = `http://3.39.6.41:8000/static/images/${image_file}.png`;
  return (
    <>
      <Img src={IMG_URL} />
      <p>{value}</p>
    </>
  );
}

export default Chart;
