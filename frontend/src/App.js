import { useEffect, useState } from "react";
import api from "./api";

function App() {
  const [tasks, setTasks] = useState([]);
  const [title, setTitle] = useState("");

  const loadTasks = () => {
    api.get("tasks/")
      .then(res => setTasks(res.data))
      .catch(err => console.error(err));
  };

  useEffect(() => {
    loadTasks();
  }, []);

  const createTask = () => {
    if (!title) return;

    api.post("tasks/create/", { title })
      .then(() => {
        setTitle("");
        loadTasks();
      })
      .catch(err => console.error(err));
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>Task Dependency Tracker</h2>

      <input
        placeholder="Task title"
        value={title}
        onChange={e => setTitle(e.target.value)}
      />
      <button onClick={createTask}>Add Task</button>

      <hr />

      {tasks.length === 0 && <p>No tasks yet</p>}

      {tasks.map(task => (
        <div key={task.id}>
          <b>{task.title}</b> — {task.status}
        </div>
      ))}
    </div>
  );
}

export default App;
