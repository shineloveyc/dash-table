import * as R from 'ramda';
import React from 'react';

import { memoizeOneFactory } from 'core/memoizer';

import {
    ActiveCell,
    Dataframe,
    Datum,
    IVisibleColumn,
    VisibleColumns,
    ICellFactoryOptions
} from 'dash-table/components/Table/props';
import CellInput from 'dash-table/components/CellInput';
import derivedCellEventHandlerProps from 'dash-table/derived/cell/eventHandlerProps';
import isActiveCell from 'dash-table/derived/cell/isActive';
import { colIsEditable } from 'dash-table/components/derivedState';

const mapDataframe = R.addIndex<Datum, JSX.Element[]>(R.map);
const mapRow = R.addIndex<IVisibleColumn, JSX.Element>(R.map);

const cellEventHandlerProps = derivedCellEventHandlerProps();

const getter = (
    activeCell: ActiveCell,
    columns: VisibleColumns,
    dataframe: Dataframe,
    editable: boolean,
    isFocused: boolean,
    tableId: string,
    dropdowns: any[][],
    propsFn: () => ICellFactoryOptions
): JSX.Element[][] => mapDataframe(
    (datum, rowIndex) => mapRow(
        (column, columnIndex) => {
            const active = isActiveCell(activeCell, rowIndex, columnIndex);

            const dropdown = dropdowns[rowIndex][columnIndex];
            const handlers = cellEventHandlerProps(propsFn)(rowIndex, columnIndex);

            return (<CellInput
                key={`column-${columnIndex}`}
                active={active}
                clearable={column.clearable}
                datum={datum}
                dropdown={dropdown}
                editable={colIsEditable(editable, column)}
                focused={isFocused}
                property={column.id}
                tableId={tableId}
                type={column.type}
                value={datum[column.id]}
                {...handlers}
            />);
        },
        columns
    ),
    dataframe
);

export default memoizeOneFactory(getter);
