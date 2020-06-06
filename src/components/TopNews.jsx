import React from 'react';
import {Container,Col,Row,Card,CardDeck,CardColumns} from 'react-bootstrap';
import CardDisplay from './CardDisplay';

class TopNews extends React.Component{

    constructor(props) {
        super(props);
        this.state = { topNewsResults : []};
    }


   componentDidMount(){
       console.log('Top News Url : --->',process.env.REACT_APP_TOPNEWS_URL)
      fetch(process.env.REACT_APP_TOPNEWS_URL)
    .then(response => response.json())
    .then(data => {
        this.setState({
            topNewsResults : data.headlines

        })
    });


   }


    render() {
        return (
            <div>
                  <CardDisplay feedResults={this.state.topNewsResults}/>

            </div>
        
        );
      }

}

export default TopNews