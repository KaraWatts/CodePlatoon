import { useEffect, useState } from "react";
import axios from "axios";
import CharCard from "../components/CharCard";
import { useOutletContext } from "react-router-dom";

const AllCharactersPage = () => {
  const [characters, setCharacters] = useState([]);
  const { setFavorites,favorites } = useOutletContext();

  const getAllCharacters = async () => {
    let response = await axios.get("https://thronesapi.com/api/v2/Characters");
    console.log(response.data);
    setCharacters(response.data);
  };

  useEffect(() => {
    getAllCharacters();
  }, []);

  return (
    <>
      <h2>All Characters</h2>
      {characters.map((char, idx) => (
        <CharCard
          key={idx}
          id={char.id}
          name={char.fullName}
          image={char.imageUrl}
          setFavorites={setFavorites}
          favorites={favorites}
        />
      ))}
    </>
  );
};

export default AllCharactersPage;
