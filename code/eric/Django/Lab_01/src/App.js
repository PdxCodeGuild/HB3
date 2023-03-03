import React, { Component } from "react";
import Modal from "./components/Modal";
import axios from "axios";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      viewCompleted: false,
      groceryList: [],
      modal: false,
      activeItem: {
        title: "",
        category: "",
        date_completed: "",
        completed: false,
      },
    };
  }

  componentDidMount() {
    this.refreshList();
  }

  refreshList = () => {
    //let csrf_token = document.querySelector("input[name=csrfmiddlewaretoken]").value;
    //const config = { headers: { 'X-CSRFToken': csrf_token }}
    axios
      .get("/api/lists/")//, config
      .then((res) => this.setState({ groceryList: res.data }))
      .catch((err) => console.log(err));
  };

  toggle = () => {
    this.setState({ modal: !this.state.modal });
  };

  handleSubmit = (item) => {
    this.toggle();
    
    if(item.id) {
      //let date_completed = document.querySelector("#completed:checked").value
      //if (date_completed === "on") {
      //  item.date_completed=Date.now().toISOString()
      //  console.log(item.date_completed)
      axios
        .put(`/api/lists/${item.id}/`, item)
        .then((res) => this.refreshList());
      return;
    }
    console.log(item)
    axios
      .post("/api/lists/", item)
      .then(window.location.reload());
  };

  handleDelete = (item) => {
    axios
      .delete(`/api/lists/${item.id}/`)
      .then((res) => this.refreshList());
  };

  createItem = () => {
    const item = { title: "", category: "", completed: false, };
    this.setState({ activeItem: item, modal: !this.state.modal });
  };

  editItem = (item) => {
    this.setState({ activeItem: item, modal: !this.state.modal });
  };

  displayCompleted = (status) => {
    if (status) {
      return this.setState({ viewCompleted: true });
    }

    return this.setState({ viewCompleted: false });
  };

  renderTabList = () => {
    return (
      <div className="nav nav-tabs">
        <span className={this.state.viewCompleted ? "nav-link active" : "nav-link"} onClick={() => this.displayCompleted(true)}>Complete</span>
        <span className={this.state.viewCompleted ? "nav-link" : "nav-link active"} onClick={() => this.displayCompleted(false)}>Incomplete</span>
      </div>
    );
  };

  renderItems = () => {
    const { viewCompleted } = this.state;
    const newItems = this.state.groceryList.filter((item) => item.completed === viewCompleted);

    return newItems.map((item) => (
      <li key={item.id} className="list-group-item d-flex justify-content-between align-items-center">
        <span className={`list-title mr-2 ${this.state.viewCompleted ? "completed-list" : ""}`} title={item.category}>{item.title} {item.date_completed}</span>
        <span>
          <button className="btn btn-secondary mr-2" onClick={() => this.editItem(item)}>Edit</button>
          <button className="btn btn-danger" onClick={() => this.handleDelete(item)}>Delete</button>
        </span>
      </li>
    ));
  };

  render() {
    return (
      <main className="container">
        <h1 className="text-white text-uppercase text-center my-4">Grocery List</h1>
        <div className="row">
          <div className="col-md-6 col-sm-10 mx-auto p-0">
            <div className="card p-3">
              <div className="mb-4">
                <button className="btn btn-primary" onClick={this.createItem}>Add Item</button>
              </div>
              {this.renderTabList()}
              <ul className="list-group list-group-flush border-top-0">
                {this.renderItems()}
              </ul>
            </div>
          </div>
        </div>
        {this.state.modal ? (<Modal activeItem={this.state.activeItem} toggle={this.toggle} onSave={this.handleSubmit}/>) : null}
      </main>
    );
  }
}

export default App;