import React, { useState } from 'react';
import { useRecoilValue } from 'recoil';
import styled from 'styled-components';
import { visualizationDatas } from '../../atoms/atom';
import Chart from './chart/Chart';

const SummaryWrapper = styled.div``;

const TapBtn = styled.button``;

function Visualization() {
  // const { isLoading, data } = useQuery('visualization', getVisialization);
  // console.log(data);

  const visualData = useRecoilValue(visualizationDatas);

  console.log(visualData);

  const [activeTab, setActiveTab] = useState(0);

  const handleTabClick = (index: number) => {
    setActiveTab(index);
  };

  return (
    <>
      <h1>visualization</h1>
      <SummaryWrapper>
        {visualData?.map((data: any, index: number) => (
          <TapBtn
            key={index}
            onClick={() => handleTabClick(index)}
            style={{
              backgroundColor: index === activeTab ? 'lightblue' : 'white',
            }}
          >
            {index + 1}
          </TapBtn>
        ))}
      </SummaryWrapper>
      {
        <Chart
          image_file={visualData[activeTab].content[0].image_file.file_id}
          key={visualData[activeTab].id}
          value={visualData[activeTab].content[1].text.value}
        />
      }
    </>
  );
}

export default Visualization;
