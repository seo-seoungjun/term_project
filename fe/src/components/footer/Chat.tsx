import React from 'react';
import styled from 'styled-components';

const ChatWrapper = styled.div`
  display: flex;
`;
const ChatInput = styled.input``;
const SubmitBtn = styled.button``;

function Chat({ register }: any) {
  return (
    <>
      <ChatWrapper>
        <ChatInput {...register('user_message')} />
        <SubmitBtn type="submit">제출</SubmitBtn>
      </ChatWrapper>
    </>
  );
}

export default Chat;
