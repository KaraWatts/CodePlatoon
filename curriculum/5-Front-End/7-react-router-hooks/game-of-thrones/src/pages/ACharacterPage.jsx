import { useEffect, useState } from "react";
import { useOutletContext, useParams } from "react-router-dom";
import axios from "axios";

const ACharacterPage = () => {
  const [character, setCharacter] = useState({});
  const { id } = useParams();
  const { setFavorites, favorites } = useOutletContext();

  const getCharacter = async () => {
    let response = await axios.get(
      `https://thronesapi.com/api/v2/Characters/${id}`
    );
    setCharacter(response.data);
  };

  useEffect(() => {
    getCharacter();
  }, []);

  return (
    <>
      <h2>{character.fullName}</h2>
      <img src={character.imageUrl} />
      <ul>
        Details
        <li>title: {character.title}</li>
        <li>family: {character.family}</li>
      </ul>
      <button onClick={()=>setFavorites([...favorites, {"id":id, "name":character.fullName, "image":character.imageUrl}])}>
        Favorite
      </button>
    </>
  );
};

export default ACharacterPage;
