import React, { Component } from "react";
import {
    Button,
    Modal,
    ModalHeader,
    ModalBody,
    ModalFooter,
    Form,
    FormGroup,
    Input,
    Label,
} from "reactstrap";

export default class CustomModal extends Component {
    constructor(props) {
        super(props);
        this.state = {
            activeItem: this.props.activeItem,
        };
    }

    handleChange = (e) => {
        let { name, value } = e.target;
        let checked_date = ''
        if (e.target.type === "checkbox") {
            value = e.target.checked;
            checked_date = new Date().toISOString().slice(0, 10)
        }
        console.log(name)
        const activeItem = { ...this.state.activeItem, [name]: value };
        activeItem.date_completed = checked_date
        console.log(activeItem)
        this.setState({ activeItem });
    };

    render() {
        const { toggle, onSave } = this.props;

        return (
            <Modal isOpen={true} toggle={toggle}>
                <ModalHeader toggle={toggle}>Grocery Item</ModalHeader>
                <ModalBody>
                    <Form>
                        <FormGroup>
                            <Label for="list-title">Items</Label>
                            <Input
                                type="text"
                                id="list-title"
                                name="title"
                                value={this.state.activeItem.title}
                                onChange={this.handleChange}
                                placeholder="Enter a grocery item"
                            />
                        </FormGroup>
                        <FormGroup>
                            <Label for="list-category">Category</Label>
                            <Input
                                type="text"
                                id="list-category"
                                name="category"
                                value={this.state.activeItem.category}
                                onChange={this.handleChange}
                                placeholder="Enter a category"
                            />
                        </FormGroup>
                        <FormGroup check>
                            <Label check>
                            <Input 
                            type="checkbox" 
                            id="completed" 
                            name="completed" 
                            checked={this.state.activeItem.completed} 
                            onChange={this.handleChange}/>Completed
                            </Label>
                        </FormGroup>
                    </Form>
                </ModalBody>
                <ModalFooter>
                    <Button color="success" onClick={() => onSave(this.state.activeItem)}>Save</Button>
                </ModalFooter>
            </Modal>
        );
    }
}