import React, { Component } from "react";
import { Table } from "reactstrap";
import NewGroupModal from "./NewGroupModal";

import ConfirmGroupRemovalModal from "./ConfirmGroupRemovalModal";

class GroupList extends Component {
  render() {
    const groups = this.props.groups;
    return (
      <Table dark>
        <thead>
          <tr>
            <th>Id</th>
            <th>Name</th>
            <th>Description</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {!groups || groups.length <= 0 ? (
            <tr>
              <td colSpan="6" align="center">
                <b>Error, please add group</b>
              </td>
            </tr>
          ) : (
            groups.map(group => (
              <tr key={group.pk}>
                <td>{group.pk}</td>
                <td>{group.name}</td>
                <td>{group.description}</td>
                <td align="center">
                  <NewGroupModal
                    create={false}
                    group={group}
                    resetState={this.props.resetState}
                  />
                  &nbsp;&nbsp;
                  <ConfirmGroupRemovalModal
                    pk={group.pk}
                    resetState={this.props.resetState}
                  />
                </td>
              </tr>
            ))
          )}
        </tbody>
      </Table>
    );
  }
}

export default GroupList;