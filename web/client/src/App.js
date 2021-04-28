import './App.css';
import {useEffect, useState} from "react";

function App() {
	const [records, setRecords] = useState([]);

	async function fetchRecords(){
		const response = await fetch("/records");
		setRecords(await response.json());
	}

	useEffect(() => {
		fetchRecords();

		const interval = setInterval(() => fetchRecords(), 10000);

		return () => clearInterval(interval);
	}, []);

	console.log(records);
  return (
    <div>
      Nombre d'entrée : {records.length}
    </div>
  );
}

export default App;
