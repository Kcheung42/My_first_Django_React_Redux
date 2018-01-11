import React from 'react'
import PropTypes from 'prop-types'

const Todo = ({onClick, completed, task}) => (
	<li
		onClick={onClick}
		style={{
			textDecoration: completed ? 'line-through' : 'none'
		}}
	>
		{task}
	</li>
)

export default Tod
