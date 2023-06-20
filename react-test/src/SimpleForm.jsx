import React from "react";
import Greetings from "./Greetings";

// class SimpleForm extends React.Component {
//   render() {
//     return (
//       <div>
//         <input type="text" name="firstName" />
//         <Greetings firstName="John" />
//       </div>
//     );
//   }
// }

class SimpleForm extends React.Component {  // объявляем класс основанный на React.Component, чтобы в нём наследовались возможности
  state = {  // функция содержащяя состояния
    firstName: "", // пременная с присвоенным значением
    firstNameError: "",
  };

  validateName = name => {  //функция валидации имен с входящим аргументом name
    const regex = /[A-Za-z]{3,}/; // регулярное выражение (символы и количество)

    return !regex.test(name) // обявление о том что функция возвращает результат тернарного оператора с условием, что булевый перевёрнутый возврат метода test(сравнивает name с множеством regex) перевёрнут для точной проерки.
      ? "The name must contain at least three letters. Numbers and special characters are not allowed."
      : "";
  };

  onFirstNameBlur = () => {
    const { firstName } = this.state;

    const firstNameError = this.validateName( firstName );

    return this.setState({ firstNameError });
  };

  onFirstNameChange = event =>
    this.setState({
      firstName: event.target.value
    });
  
  render() {
    const { firstNameError, firstName } = this.state;
    return (
      <div>
        <div>
          <label>
            First name:
            <input
              type="text"
              name="firstName"
              onChange={this.onFirstNameChange}
              onBlur={this.onFirstNameBlur}
            />
            {firstNameError && <div>{firstNameError}</div>}
          </label>
        </div>

        <Greetings
          firstName={firstName}
        />
      </div>
    );
  }
}
//     return (
//       <div>
//         <input type="text" name="firstName" onChange={this.onFirstNameChange} />

//         <Greetings firstName={this.state.firstName} />
//       </div>
//     );
//   }
// }


export default SimpleForm;