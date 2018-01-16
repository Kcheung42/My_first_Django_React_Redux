// ************************************************************************** //
//                                                                            //
//                                                        :::      ::::::::   //
//   HelloWorld.jsx                                     :+:      :+:    :+:   //
//                                                    +:+ +:+         +:+     //
//   By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+        //
//                                                +#+#+#+#+#+   +#+           //
//   Created: 2018/01/15 13:57:36 by kcheung           #+#    #+#             //
//   Updated: 2018/01/15 14:05:01 by kcheung          ###   ########.fr       //
//                                                                            //
// ************************************************************************** //

import React from 'react';

export class HelloWorld extends React.Component {
	render(){
		return(
				<div>
					Hello {this.props.children}
				</div>
				)
	}
}
