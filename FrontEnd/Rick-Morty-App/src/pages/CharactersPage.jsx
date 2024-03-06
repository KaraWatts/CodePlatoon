import CharacterCard from "../components/CharacterCard"
import { useState, useEffect } from "react";
import axios from "axios";
import { Button } from "react-bootstrap";

function Characters () {
    const [characters, setCharacters] = useState({})
    const [page, setpage] = useState(1)
    const [numOfPages, setNumOfPages] = useState()
    
    useEffect(() => {
        const callResponse = async () => {
            
                const url = `https://rickandmortyapi.com/api/character/?page=${page}`;
                const response = await axios.get(url);
                setNumOfPages(response.data.info.pages)
                setCharacters(response.data.results)
                
                
        }
        callResponse()
         }, [page])
         console.log(`Characters:`, characters)
         
       
   
        
    return (
        <>
        <h2>These are characters</h2>
        <CharacterCard />
        <div >
        <Button variant="outline-secondary" style={{marginRight:"2rem"}} onClick={() => page > 1 ? setpage(page - 1) : alert("Thats all the characters")}>Prev</Button>
        <i>Page {page} </i>
        <Button variant="outline-secondary" style={{marginLeft:"2rem"}} onClick={() => page < numOfPages ? setpage(page + 1) : alert("Thats all the characters")}>Next</Button>
        </div>
        </>
    )
}

export default Characters;




// const myPromises = [];
//             for (let i = 1; i <= 5; i++) {
//                 const url = `https://rickandmortyapi.com/api/character/?page=${i}`;
//                 const promiseObject = axios.get(url);
//                 myPromises.push(promiseObject);
//                 console.log("promise objects ", promiseObject)
//             }

//             const allResponses = await Promise.all(myPromises);
            
//             const data = allResponses.reduce( (acc, page) => {


//                 acc = [...acc, ...page.data.results];
//                 return acc;
//             }, []);
//             console.log("data", data);


 // console.log(numOfPages)

            // axios
            //     .request(`https://rickandmortyapi.com/api/character/`)
            //     .then((reponse) => response.data.info.next ?)
            //     .then(function (response) {
            //         let responseData = response.data
            //         console.log(responseData)
            //     })
           
        // }
        // callResponse()