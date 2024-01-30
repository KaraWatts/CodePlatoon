import { useState } from "react";

const Task = ({taskTitle, taskId, taskCompleted}) => {

  const [checked, setChecked] = useState(taskCompleted)
  
  return (
    <li >
      <input
        type="checkbox"
        checked={checked}
        onChange={(e)=>setChecked(e.target.checked)}
        // onChange={(e) =>
        //   setTasks(
        //     tasks.map((item) => {
        //       if (item.id === task.id) {
        //         item.completed = e.target.checked;
        //         return item;
        //       } else {
        //         return item;
        //       }
        //     })
        //   )
        // }
      />
        {taskTitle}
    </li>
  );
};

export default Task;
