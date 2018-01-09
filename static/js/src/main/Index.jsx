import React from 'react';
import { render } from 'react-dom';
import { HelloWorld } from './components/HelloWorld';
import { App1Container } from './containers/App1Container';
import { changeName, addToDo } from './actions';
import { reducers } from './reducers';
import { createStore } from 'redux';

// const reducer = function(state, action){
//   if (action.type == 'INC'){
//     return state + action.payload
//   }
//   if (action.type == 'DEC'){
//     return state - action.payload
//   }
//   return state;
// }
//

// const store = createStore(reducer, 0);
const store = createStore(reducers);

store.subscribe(() => {
  console.log("store changed", store.getState())
})

//Bound ActionCreator
const boundChangeName = text => dispatch(changeName("Bambi"))

// store.dispatch({type: "INC", payload: 1})
// store.dispatch({type: "DEC", payload: 100})

store.dispatch(changeName('Bambi'))
store.dispatch(changeName('Cheung'))
store.dispatch({type: "CHANGE_AGE", payload: 27})
store.dispatch({type: "CHANGE_AGE", payload: 21})
store.dispatch({type: "CHANGE_AGE", payload: 33})
store.dispatch(addToDo('My first task'))

render(<App1Container />, document.getElementById('react-root'))
