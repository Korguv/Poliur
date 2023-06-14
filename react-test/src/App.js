import logo from './logo.svg';
import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// import Greetings from "./Greetings";
// const App = () => (
//   <div>
//     <Greetings firstName="John" lastName="Smith" />
//   </div>
// );

import SimpleForm from "./SimpleForm";
const App = () => (
  <div>
    <SimpleForm />
  </div>
);


export default App;