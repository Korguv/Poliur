'use strict';
// модальные окна
alert ('Окно уведомление'); // Окно с сообщением
let first = promt ("Вопрос","предустановленное значение"); // вопрос со строкой ответа
let second = confirm ("Подтверждение"); // Булевый вопрос

alert( 5 % 2 ); // 1, остаток от деления 5 на 2
alert( 8 % 3 ); // 2, остаток от деления 8 на 3
alert( 8 % 4 ); // 0, остаток от деления 8 на 4

alert( 2 ** 2 ); // 2² = 4
alert( 2 ** 3 ); // 2³ = 8
alert( 2 ** 4 ); // 2⁴ = 16
alert( 4 ** (1/2) ); // 2 (степень 1/2 эквивалентна взятию квадратного корня)
alert( 8 ** (1/3) ); // 2 (степень 1/3 эквивалентна взятию кубического корня)


// Не влияет на числа
let x = 1;
alert( +x ); // 1

let y = -2;
alert( +y ); // -2

// Преобразует не числа в числа
alert( +true ); // 1
alert( +"" );   // 0

let counter = 1;
let a = ++counter; // (*)
alert(a); // 2
let counter = 1;
let a = counter++; // (*) меняем ++counter на counter++
alert(a); // 1


    AND(и) ( & )
    OR(или) ( | )
    XOR(побитовое исключающее или) ( ^ )
    NOT(не) ( ~ )
    LEFT SHIFT(левый сдвиг) ( << )
    RIGHT SHIFT(правый сдвиг) ( >> )
    ZERO-FILL RIGHT SHIFT(правый сдвиг с заполнением нулями) ( >>> )


let year = prompt('В каком году была опубликована спецификация ECMAScript-2015?', '');
if (year == 2015) {
  alert( 'Да вы знаток!' );
} else {
  alert( 'А вот и неправильно!' ); // любое значение, кроме 2015
}

let year = prompt('В каком году была опубликована спецификация ECMAScript-2015?', '');
if (year < 2015) {
  alert( 'Это слишком рано...' );
} else if (year > 2015) {
  alert( 'Это поздновато' );
} else {
  alert( 'Верно!' );
}

let result = условие ? значение1 : значение2;
let accessAllowed = (age > 18) ? true : false;
// оператор сравнения "age > 18" выполняется первым в любом случае
// (нет необходимости заключать его в скобки)
let accessAllowed = age > 18 ? true : false;

let age = prompt('Возраст?', 18);
let message = (age < 3) ? 'Здравствуй, малыш!' :
  (age < 18) ? 'Привет!' :
  (age < 100) ? 'Здравствуйте!' :
  'Какой необычный возраст!';
alert( message );

for (let i = 0; i < 10; i++) {

  // если true, пропустить оставшуюся часть тела цикла
  if (i % 2 == 0) continue;

  alert(i); // 1, затем 3, 5, 7, 9
}

let sum = 0;

while (true) {

  let value = +prompt("Введите число", '');

  if (!value) break; // (*)

  sum += value;

}
alert( 'Сумма: ' + sum );


outer: for (let i = 0; i < 3; i++) {

    for (let j = 0; j < 3; j++) {
  
      let input = prompt(`Значение на координатах (${i},${j})`, '');
  
      // если пустая строка или Отмена, то выйти из обоих циклов
      if (!input) break outer; // (*)
  
      // сделать что-нибудь со значениями...
    }
  }
  
  alert('Готово!');

  let a = 2 + 2;

switch (a) {
  case 3:
    alert( 'Маловато' );
    break;
  case 4:
    alert( 'В точку!' );
    break;
  case 5:
    alert( 'Перебор' );
    break;
  default:
    alert( "Нет таких значений" );
}