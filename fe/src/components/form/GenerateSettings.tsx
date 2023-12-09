import React from 'react';
import { useRecoilValue } from 'recoil';
import styled from 'styled-components';
import { generateSettingsMinMaxValue } from '../../atoms/atom';

const GenerateSettingsWrapper = styled.div`
  position: fixed;
  left: 0;
  top: 0;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100vw;
  height: 100vh;
  z-index: 10;
  background-color: ${(prop) => prop.theme.blurBgColor};
  opacity: 0.8;
`;

const GenerateSetting = styled.div`
  width: 50%;
  height: 40%;
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  border-radius: 15px;
  border: 1px solid black;
  background-color: ${(props) => props.theme.bgColor};
`;
const LeftSide = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
`;
const RightSide = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  input {
    margin-bottom: 20px;
  }
`;

const MaxTokensInput = styled.input``;
const TemperatureInput = styled.input``;
const NumberMessagesInput = styled.input``;
const PresencePenaltyInput = styled.input``;
const FrequencyPenaltyInput = styled.input``;
const ToggleBtn = styled.div`
  border-radius: 4px;
  border: 1px solid black;
  padding: 2px;
  cursor: pointer;
  margin-top: 20px;
  background-color: ${(props) => props.theme.bgColor};
`;

export function GenerateSettings({ register, toggle }: any) {
  const minMaxValue = useRecoilValue(generateSettingsMinMaxValue);
  const onToggleBtnClick = () => {
    toggle((cur: boolean) => !cur);
  };
  return (
    <GenerateSettingsWrapper>
      <GenerateSetting>
        <LeftSide>
          <p>Model Provider: Local Provider</p>
          <p>Model: Code llama-fine-tuning Model</p>
        </LeftSide>
        <RightSide>
          <p>max_tokens</p>
          <MaxTokensInput
            {...register('max_tokens')}
            min={minMaxValue.maxToken.min}
            max={minMaxValue.maxToken.max}
            type="range"
          />
          <p>temperature</p>
          <TemperatureInput
            min={minMaxValue.temperature.min}
            max={minMaxValue.temperature.max}
            {...register('temperature')}
            type="range"
          />
          <p>number_messages</p>
          <NumberMessagesInput
            min={minMaxValue.numberMessages.min}
            max={minMaxValue.numberMessages.max}
            {...register('number_messages')}
            type="range"
          />
          <p>presence_penalty</p>
          <PresencePenaltyInput
            min={minMaxValue.presencePenalty.min}
            max={minMaxValue.presencePenalty.max}
            {...register('presence_penalty')}
            type="range"
          />
          <p>frequency_penalty</p>
          <FrequencyPenaltyInput
            min={minMaxValue.frequencyPenalty.min}
            max={minMaxValue.frequencyPenalty.max}
            {...register('frequency_penalty')}
            type="range"
          />
        </RightSide>
      </GenerateSetting>
      <ToggleBtn onClick={onToggleBtnClick}>확인</ToggleBtn>
    </GenerateSettingsWrapper>
  );
}

export default GenerateSettings;
