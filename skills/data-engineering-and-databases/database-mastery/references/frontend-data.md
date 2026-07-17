# Frontend Data Apps

## Table of Contents
- React fundamentals
- Fetching data
- Tables
- Charts
- State and filters

## React fundamentals

React apps are built from components. Official docs emphasize components, JSX, rendering lists/conditions, event handling, and shared state. Source: https://react.dev/learn

## Fetching data

Keep loading, error, empty, and success states explicit. Abort stale requests when filters change quickly.

## Tables

Separate data, sorting, filtering, and rendering. For big tables, use server-side pagination.

## Charts

The API should return chart-friendly rows. Keep chart components dumb.

## State and filters

URL query parameters are useful for shareable dashboard states. Centralize filters and pass them to query hooks.

Usage image: build frontend data apps when the user needs interaction. Watch hidden loading failures. Avoid embedding business calculations only in the browser.
