export const CHANGE_NAME = 'CHANE_NAME'
export const CHANGE_AGE = 'CHANGE_AGE'
export const ADD_TODO = 'ADD_TODO'
export const TOGGLE_TODO = 'TOGGLE_TODO'
export const SET_VISIBILITY_FILTER = 'SET_VISIBILITY_FILTER'

export function changeName(payload){
	return {type: CHANGE_NAME, payload }
}

export function changeAge(payload){
	return { type: CHANGE_AGE, payload }
}

export const VisibilityFilters = {
	SHOW_ALL: 'SHOW_ALL',
	SHOW_COMPLETED: 'SHOW_COMPLETED',
	SHOW_ACTIVE: 'SHOW_ACTIVE',
}

let nextTodoId = 0
export function addToDo(payload){
	return {
		type: ADD_TODO,
		id: nextTodoId++,
		payload
	}
}

export function toggleToDo(payload){
	return { type: TOGGLE_TODO, payload }
}

export function setVisibilityFilter(payload){
	return { type: SET_VISIBILITY_FILTER, payload }
}
