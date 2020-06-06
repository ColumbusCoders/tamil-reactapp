import React from 'react';
import {Container,Col,Row,Card,CardDeck,CardColumns} from 'react-bootstrap';
import CardDisplay from './CardDisplay';

class Cinema extends React.Component{

    constructor(props) {
        super(props);
        this.state = { NewsResults : []};
    }


   componentDidMount(){

    console.log('Cinema Url : --->',process.env.REACT_APP_CINEMA_URL)
    fetch(process.env.REACT_APP_CINEMA_URL)
    .then(response => response.json())
    .then(data => {
        this.setState({
            NewsResults : data.headlines
        })
    });


   }


    render() {
        let tst = this.state.NewsResults;
        tst.filter(name => name.category === 'Cinema')
        console.log('TEsting ' , tst)
        return (
            <div>
                  <CardDisplay feedResults={this.state.NewsResults}/>

            </div>
        
        );
      }

}

export default Cinema