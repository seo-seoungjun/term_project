import React, { useEffect } from 'react';
import styled from 'styled-components';
import Visualization from '../components/analytics/Visualization';
import { useRecoilState } from 'recoil';
import { isDataExist, resultDatas, visualizationDatas } from '../atoms/atom';
import SideBar from '../components/navbar/SideBar';
import { useLocation } from 'react-router-dom';
import { useForm } from 'react-hook-form';

const DATA_KEY = 'data';

const Section = styled.section`
  width: 70%;
`;

function Analytics() {
  const [resultData, setResultData] = useRecoilState(resultDatas);
  const [isData, setIsData] = useRecoilState(isDataExist);
  const [visualizationData, setVisualizationData] =
    useRecoilState(visualizationDatas);

  const {
    register,
    handleSubmit,
    formState: { errors },
    setError,
  } = useForm();

  const { state } = useLocation<any>();

  useEffect(() => {
    if (state?.data !== undefined) {
      setResultData(state.data);
      localStorage.setItem(DATA_KEY, JSON.stringify(state.data));
      const imgData = state.data.filter(
        (data: any) => data.content[0].type === 'image_file'
      );
      setVisualizationData(imgData);
      setIsData(true);
    } else {
      if (localStorage.getItem(DATA_KEY) !== null) {
        setResultData(JSON.parse(localStorage.getItem(DATA_KEY) || ''));
        const imgData = JSON.parse(localStorage.getItem(DATA_KEY) || '').filter(
          (data: any) => data.content[0].type === 'image_file'
        );
        setVisualizationData(imgData);
        setIsData(true);
      }
    }
  }, []);

  console.log(resultData);
  console.log(visualizationData);

  return (
    <>
      {isData ? (
        <>
          <SideBar />
          <Section>
            <Visualization />
          </Section>
        </>
      ) : (
        '파일을 제출해 주세요'
      )}
    </>
  );
}

export default Analytics;
