import tasks from "./tasks.json" assert { type: "json" };
import axios from "axios";
// const tasks = require("./tasks.json")
tasks.map(({ id, task, completed } = item) => {
  console.log(id, task, completed);
});

const completedTasks = tasks.filter((task) => {
  return task.completed === true; // Only include tasks where 'completed' is true.
  //return task.completed (this is already a bool)
});

const incompleteTasks = tasks.filter((task) => {
  // return task.completed === false
  return !task.completed;
});

const getPokemon = async () => {
  let response = await axios.get("https://pokeapi.co/api/v2/pokemon/ditto");
  console.log(response.data.sprites.front_default);
};

getPokemon();
