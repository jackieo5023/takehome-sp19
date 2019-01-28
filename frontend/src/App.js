import React, { Component } from 'react'
import Instructions from './Instructions'
import Counter from './Counter'
import Show from './Show'

class App extends Component {
  constructor(props) {
    super(props)
    this.state = {
      shows: [
        {id: 1, name: "Game of Thrones", episodes_seen: 0},
        {id: 2, name: "Naruto", episodes_seen: 220},
        {id: 3, name: "Black Mirror", episodes_seen: 3},
      ],
      newShow: ""
    }
  }

  handleInputChange = event => {
    this.setState({
      newShow: event.target.value
    });
  }

  handleSubmit = () => {
    let updated_shows = this.state.shows
    updated_shows.push({
      id: this.state.shows.length + 1,
      name: this.state.newShow,
      episodes_seen: 0
    });

    this.setState({
      shows: updated_shows,
      newShow: ""
    });
  }

  render() {
    return (
      <div className="App">
        <Instructions complete={true}/>
        {this.state.shows.map(x => (
          <div>
            <Show id={x.id} name={x.name} episodes_seen={x.episodes_seen} />
            <Counter initialCount={x.episodes_seen} />
          </div>
        ))}
        <input 
          type="text"
          value={this.state.newShow}
          onChange={this.handleInputChange}
        />
        <button onClick={this.handleSubmit}>Submit</button>
      </div>
    )
  }
}

export default App
