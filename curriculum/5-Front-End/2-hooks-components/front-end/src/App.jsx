import { useState, useEffect } from "react";
import jsonTasks from "./data/tasks.json";
import "./App.css";
import Task from "./components/Task.jsx";

function App() {
  //         get    sets           init
  // const [hello, setHello] = useState("Hello Victor") //any||null
  const [tasks, setTasks] = useState(jsonTasks); // returns a array [getter, setter]
  const [formInput, setFormInput] = useState("");
  // const [show, setShow] = useState(true);
  const formSubmit = (e) => {
    e.preventDefault();
    let newTask = { id: tasks.length + 1, task: formInput, completed: false };
    setTasks([...tasks, newTask]);
    setFormInput("");
  };

  // useEffect(()=>{
  //   console.log(show)
  // }, [show])
  // if and else
  // x if x > y else y
  // ternirary statement
  //  x > y ? x : y
  return (
    <>
      {/*<button onClick={()=>setShow(!show)}>Change</button>
       <div id="greeting">{hello}</div>
      <button onClick={()=>setHello("Goodbye Victor")}>
        Click Me
      </button>
      {
      show ?
      <h1>Hello</h1>
      :
      <h1>Goodbye</h1>
      }
      <button onClick={()=>setShow(!show)}>Change</button>
      */}

      <form onSubmit={(e) => formSubmit(e)}>
        <input
          placeholder="enter task"
          value={formInput}
          onChange={(e) => [
            setFormInput(e.target.value),
            console.log(e.target.value),
          ]}
        />
        <button type="submit">Submit</button>
      </form>
      <ol>
        {tasks.map((task) => (
          // taskProp = {task}

          <Task key={task.id}
            taskTitle={task.task}
            taskId={task.id}
            taskCompleted={task.completed}
          />
        ))}
      </ol>
    </>
  );
}

export default App;
