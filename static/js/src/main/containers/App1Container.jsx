// ************************************************************************** //
//                                                                            //
//                                                        :::      ::::::::   //
//   App1Container.jsx                                  :+:      :+:    :+:   //
//                                                    +:+ +:+         +:+     //
//   By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+        //
//                                                +#+#+#+#+#+   +#+           //
//   Created: 2018/01/15 11:17:45 by kcheung           #+#    #+#             //
//   Updated: 2018/01/15 12:26:29 by kcheung          ###   ########.fr       //
//                                                                            //
// ************************************************************************** //

import React from 'react';
import { HelloWorld } from '../components/HelloWorld'
import { Button } from '../components/Button'
import { Toggle } from '../components/Toggle'
import  VisibleTdoList  from  './VisibileTodoList'
// import  {VisibleTdoList}  from  './VisibileTodoList'
import  Footer  from  '../components/Footer'
import AddTodo from './AddTodo'

export class App1Container extends React.Component{
	render(){
		return(
			<div>
				<HelloWorld>Bambi</HelloWorld>
				<Button label="Buton Component">Bambi</Button>
				<Toggle />
				<Footer />
				<VisibleTdoList />
				<AddTodo />
			</div>
		);
	}
}
