// src/features/filters/filterSlice.ts
import { createSlice, PayloadAction } from '@reduxjs/toolkit';

interface FilterState {
  name: string;
  minPrice: number;
  maxPrice: number;
  fromDate: string;
  toDate: string;
}

const initialState: FilterState = {
  name: '',
  minPrice: 0,
  maxPrice: Infinity,
  fromDate: '',
  toDate: ''
};

const filterSlice = createSlice({
  name: 'filters',
  initialState,
  reducers: {
    setNameFilter(state, action: PayloadAction<string>) {
      state.name = action.payload;
    },
    setMinPriceFilter(state, action: PayloadAction<number>) {
      state.minPrice = action.payload;
    },
    setMaxPriceFilter(state, action: PayloadAction<number>) {
      state.maxPrice = action.payload;
    },
    setFromDateFilter(state, action: PayloadAction<string>) {
      state.fromDate = action.payload;
    },
    setToDateFilter(state, action: PayloadAction<string>) {
      state.toDate = action.payload;
    },
    resetFilters(state) {
      return initialState;
    }
  }
});

export const {
  setNameFilter,
  setMinPriceFilter,
  setMaxPriceFilter,
  setFromDateFilter,
  setToDateFilter,
  resetFilters
} = filterSlice.actions;

export default filterSlice.reducer;