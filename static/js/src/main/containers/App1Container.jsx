import React from 'react';
import { HelloWorld } from '../components/HelloWorld'
import { Button } from '../components/Button'
import { Toggle } from '../components/Toggle'

export class App1Container extends React.Component{
	toggleShowing = () => {
		this.setState({
			isShowing: !this.state.isShowing
		})
	}

	render(){
		return(
				<div>
						<HelloWorld>Bambi</HelloWorld>
						<Button label="Buton Component">Bambi</Button>
						<Toggle />
				</div>
		);
	}
}
