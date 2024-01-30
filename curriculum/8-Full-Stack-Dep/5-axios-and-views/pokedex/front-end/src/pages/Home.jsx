import Row from "react-bootstrap/esm/Row";

export const Home = () => {
  return (
    <Row style={{ textAlign: "center", padding: "0 10vmin" }}>
      <p>
        <strong>Welcome to Code Platoons Pokedex Application!!</strong>
        <br />
        In this application users will be able to view Pokedex information of a
        limited amount of Pokemon. We are still on our first version, but as we
        build up our Database we are sure more and more useful information will
        be provided by this application.
      </p>
    </Row>
  );
};
