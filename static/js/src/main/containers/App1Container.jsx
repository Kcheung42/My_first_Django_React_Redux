import React from 'react';
import { HelloWorld } from '../components/HelloWorld'
import { Button } from '../components/Button'
import { Toggle } from '../components/Toggle'
import  VisibleTdoList  from  './VisibileTodoList'
import  Footer  from  '../components/Footer'

export class App1Container extends React.Component{
	render(){
		return(
			<div>
				<HelloWorld>Bambi</HelloWorld>
				<Button label="Buton Component">Bambi</Button>
				<Toggle />
				<VisibleTdoList />
				<Footer />
			</div>
		);
	}
}
