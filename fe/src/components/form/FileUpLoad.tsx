import React, { useState } from 'react';
import styled from 'styled-components';
import Chat from '../footer/Chat';
import GenerateSettings from './GenerateSettings';
import { useRecoilState, useRecoilValue } from 'recoil';
import {
  ISettings,
  fileUpLoadSettings,
  grammarSettings,
} from '../../atoms/atom';
import { useForm } from 'react-hook-form';
import { useMutation } from 'react-query';
import { submitFormApi } from '../../APIs/api';
import { Redirect } from 'react-router-dom';

const Section = styled.section`
  width: 70%;
`;

const DataForm = styled.form`
  display: flex;
  align-items: center;
  flex-direction: column;
`;
const SettingsWrapper = styled.div`
  display: flex;
  justify-content: space-between;
`;
const GrammerList = styled.select``;
const GrammerSettingsBtn = styled.div`
  border-radius: 4px;
  border: 1px solid black;
  padding: 2px;
  cursor: pointer;
`;
const FileUploadInput = styled.input``;

function FileUpLoad() {
  const [showGenerateSettings, setShowGenerateSettings] = useState(false);
  const [isSubmitSuccess, setIsSubmitsuccess] = useState(false);

  const [defaultSettings, setDefaultSettings] =
    useRecoilState(fileUpLoadSettings);

  const grammarList = useRecoilValue(grammarSettings);

  const {
    register,
    handleSubmit,
    formState: { errors },
    setError,
  } = useForm({
    defaultValues: defaultSettings,
  });

  const { mutate, isLoading, data } = useMutation(submitFormApi, {
    onSuccess: (res) => {
      console.log(res);
      setIsSubmitsuccess(true);
    },
    onError: (err) => {
      console.log(err);
    },
  });

  const SubmitOnValid = (data: ISettings) => {
    const formData = new FormData();

    data.file = data.file[0];

    for (const [key, value] of Object.entries(data)) {
      formData.append(key, value);
      console.log(key, value);
    }

    setDefaultSettings(data);
    mutate(formData);
  };

  const onSettingsClick = () => {
    setShowGenerateSettings(true);
  };

  const onSampleDataClick = () => {};

  return (
    <>
      {isSubmitSuccess ? (
        <Redirect
          to={{
            pathname: '/analytics',
            state: data,
          }}
        />
      ) : isLoading ? (
        'Loading'
      ) : (
        <Section>
          <DataForm
            encType="multipart/form-data"
            onSubmit={handleSubmit(SubmitOnValid)}
          >
            <SettingsWrapper>
              <GrammerList {...register('grammar')}>
                {grammarList?.map((grammar) => (
                  <option value={grammar} key={grammar}>
                    {grammar}
                  </option>
                ))}
              </GrammerList>
              <GrammerSettingsBtn onClick={onSettingsClick}>
                세팅
              </GrammerSettingsBtn>
            </SettingsWrapper>
            <FileUploadInput
              {...register('file', {
                required: 'File is Required',
                validate: (value) => {
                  const acceptedFormats = ['csv', 'json'];
                  const fileExtension = value[0]?.name
                    .split('.')
                    .pop()
                    .toLowerCase();
                  if (!acceptedFormats.includes(fileExtension)) {
                    return 'Invalid file format. Only csv or files are allowed.';
                  }
                },
              })}
              type="file"
            />
            {showGenerateSettings ? (
              <GenerateSettings
                toggle={setShowGenerateSettings}
                register={register}
              />
            ) : null}
            <Chat register={register}></Chat>
            <h1 style={{ color: 'red' }}>{errors?.file?.message as any}</h1>
          </DataForm>
        </Section>
      )}
    </>
  );
}

export default FileUpLoad;
