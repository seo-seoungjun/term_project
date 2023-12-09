import React from 'react';
import { Link, useRouteMatch } from 'react-router-dom';

import styled from 'styled-components';

const Header = styled.header`
  background-color: ${(props) => props.theme.bgColor};
  width: 30%;
  border-radius: 15px;
  border: 1px solid #555151;
  /* box-shadow: 2px 2px 2px 2px rgba(0, 0, 0, 0.25); */
  display: flex;
  justify-content: center;
  flex-direction: column;
  * {
    text-align: center;
  }
`;

const LidaIcon = styled.div``;

const MeueNav = styled.nav`
  margin-top: 70px;
`;

const MeueList = styled.ul``;

const HomeMenu = styled.li<{ $isActive: boolean }>`
  transition: all 1s;
  a {
    background-color: ${(props) =>
      props.$isActive ? props.theme.highLightColor : props.theme.bgColor};
  }
  a:hover {
    background-color: ${(props) => props.theme.highLightColor};
  }
  &.on-hover {
    background-color: ${(props) => props.theme.bgColor};
  }
`;

const DemoMenu = styled.li<{ $isActive: boolean }>`
  transition: all 1s;
  a {
    background-color: ${(props) =>
      props.$isActive ? props.theme.highLightColor : props.theme.bgColor};
  }
  a:hover {
    background-color: ${(props) => props.theme.highLightColor};
  }
  &.on-hover a {
    background-color: ${(props) => props.theme.bgColor};
  }
`;

const DataNav = styled.div`
  margin-top: 50px;
`;

const DataRecordList = styled.ul``;

const CreateNewData = styled.li``;

const Data = styled.li``;

const AuthNav = styled.div`
  margin-top: 50px;
`;

const AuthList = styled.ul``;

const SignIn = styled.li``;

const SignUp = styled.li``;

const onMouseOver = (e: React.MouseEvent<HTMLAnchorElement>) => {
  const target = e.target as HTMLAnchorElement;
  const parentEl = target.parentElement;
  const li = parentEl?.parentElement?.querySelector('#demo');
  li?.classList.add('on-hover');
};

const onMouseLeave = (e: React.MouseEvent<HTMLAnchorElement>) => {
  const target = e.target as HTMLAnchorElement;
  const parentEl = target.parentElement;
  const li = parentEl?.parentElement?.querySelector('#demo');
  li?.classList.remove('on-hover');
};

function SideBar() {
  const homeMenuMatch = useRouteMatch({ path: '/', exact: true });
  const demoMenuMatch = useRouteMatch({ path: '/demo', exact: true });

  return (
    <>
      <Header>
        <LidaIcon>
          <h1>Lida</h1>
        </LidaIcon>
        <MeueNav>
          <MeueList>
            <HomeMenu $isActive={homeMenuMatch !== null}>
              <Link
                onMouseLeave={onMouseLeave}
                onMouseOver={onMouseOver}
                to={'/'}
              >
                Home
              </Link>
            </HomeMenu>
            <DemoMenu id="demo" $isActive={demoMenuMatch !== null}>
              <Link to={'/demo'}>Demo</Link>
            </DemoMenu>
          </MeueList>
        </MeueNav>
        <DataNav>
          <DataRecordList>
            <CreateNewData>
              <p>new</p>
            </CreateNewData>
            <Data>
              <p>ect</p>
            </Data>
          </DataRecordList>
        </DataNav>
        <AuthNav>
          <p>Authentication</p>
          <AuthList>
            <SignIn>
              <p>SignIn</p>
            </SignIn>
            <SignUp>
              <p>SignUp</p>
            </SignUp>
          </AuthList>
        </AuthNav>
      </Header>
    </>
  );
}

export default SideBar;
