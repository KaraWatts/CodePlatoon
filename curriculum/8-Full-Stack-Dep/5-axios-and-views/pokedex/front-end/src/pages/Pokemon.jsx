import Row from "react-bootstrap/esm/Row";
import { useEffect, useState } from "react";
import axios from "axios";

export const Pokemon = () => {
  const [pokemon, setPokemon] = useState([]);

  const getAllPokemon = async () => {
    // request would be sent within this function
    let response = await axios
      .get("http://127.0.0.1:8000/api/v1/pokemon/")
      .catch((err) => {
        console.log(err);
        alert("something went wrong");
      });
    setPokemon(response.data);
  };

  useEffect(() => {
    getAllPokemon();
  }, []);

  return (
    <Row style={{ padding: "0 10vmin" }}>
      <h1 style={{ textAlign: "center" }}>Pokemon</h1>
      <ul>
        {pokemon.map((poke) => (
          <li
            key={poke.id}
            style={{
              margin: "3vmin",
              display: "flex",
              flexDirection: "column",
            }}
          >
            Name: {poke.name} <br /> Level: {poke.level}
            <ul>
              Moves
              {poke.moves.map((move, idx) => (
                <li key={`${poke.id}${idx}`}>{move}</li>
              ))}
            </ul>
          </li>
        ))}
      </ul>
    </Row>
  );
};
