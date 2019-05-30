module Main exposing (main)

import Browser exposing (document)
import Browser.Events
import Element exposing (Element, column, el, height, px, text, width)
import Element.Font as Font
import Html exposing (Html)
import Mark.Error
import Markup exposing (Day)
import Task


main : Program WindowSize Model Msg
main =
    document
        { init = init
        , update = update
        , view = view
        , subscriptions = subscriptions
        }



-- MODEL


type alias Model =
    { size : WindowSize }


type alias WindowSize =
    { width : Int
    , height : Int
    }


type Msg
    = SetSize WindowSize



-- INIT


init : WindowSize -> ( Model, Cmd Msg )
init size =
    ( { size = size }, Cmd.none )



-- UPDATE


update : Msg -> Model -> ( Model, Cmd Msg )
update msg model =
    case msg of
        SetSize size ->
            ( { size = size }, Cmd.none )



-- VIEW


view : Model -> Browser.Document Msg
view model =
    { title = ""
    , body = [ Element.layout [] (body model) ]
    }


type Layout
    = Wide
    | Narrow


body : Model -> Element Msg
body model =
    let
        layout =
            if toFloat model.size.width / toFloat model.size.height > 1.3 then
                Wide

            else
                Narrow
    in
    case Markup.parseDocument daysString of
        Ok days ->
            column [ Element.centerX ] (List.map (dayElement layout) days)

        Err [] ->
            Element.text "There were errors but there are no errors..."

        Err (firstError :: _) ->
            Element.text (Debug.toString <| Mark.Error.toDetails firstError)


dayElement : Layout -> Day Msg -> Element Msg
dayElement layout day =
    let
        title_ =
            dayTitle day.day day.title

        content =
            List.map image day.images
    in
    case layout of
        Narrow ->
            Element.column []
                [ title_
                , day.description
                , Element.column [] content
                ]

        Wide ->
            Element.row []
                [ Element.column [] content
                , Element.column []
                    [ title_
                    , day.description
                    ]
                ]


dayTitle : Int -> String -> Element Msg
dayTitle day title_ =
    el [ Element.onLeft (title (String.fromInt day ++ ". ")) ] (title title_)


title : String -> Element Msg
title string =
    el [ Font.size 24, Font.bold ] (text string)


image : String -> Element Msg
image src =
    Element.image [ width (px 500), height (px 500) ]
        { src = src, description = "" }



-- SUBSCRIPTIONS


subscriptions : Model -> Sub Msg
subscriptions model =
    Browser.Events.onResize (\wd ht -> SetSize { width = wd, height = ht })



-- CONTENT


daysString : String
daysString =
    """

|> Day
    day = 1
    name = Air Conditioner
    description =
        I started this project by learning [Processing]{link|url=https://processing.org},
        so naturally the first day was inspired by
        [the tutorial]{link|url=https://processing.org/tutorials/gettingstarted/} I used.
    images =
        |> Image
            img/day_01.png

|> Day
    day = 2
    name = Julia
    description =
        Hey
    images =
        |> Image
            img/day_02.png

|> Day
    day = 3
    name = Circles
    description =
        Hey
    images =
        |> Image
            img/day_03.png

|> Day
    day = 4
    name = Bouquet
    description =
        Hey
    images =
        |> Image
            img/day_04.png

|> Day
    day = 5
    name = Spirals
    description =
        Hey
    images =
        |> Image
            img/day_05.mov

|> Day
    day = 6
    name = Maze Complement
    description =
        Hey
    images =
        |> Image
            img/day_06.png

|> Day
    day = 7
    name = Pixels
    description =
        Hey
    images =
        |> Image
            img/day_07.png

|> Day
    day = 8
    name = Squares
    description =
        Hey
    images =
        |> Image
            img/day_08.png

|> Day
    day = 9
    name = Triangles
    description =
        Hey
    images =
        |> Image
            img/day_09.png

|> Day
    day = 10
    name = Tsuro
    description =
        Hey
    images =
        |> Image
            img/day_10.png

|> Day
    day = 11
    name = Blokus
    description =
        Hey
    images =
        |> Image
            img/day_11.png

|> Day
    day = 12
    name = Terrain
    description =
        Hey
    images =
        |> Image
            img/day_12.png

|> Day
    day = 13
    name = Topography
    description =
        Hey
    images =
        |> Image
            img/day_13.png

|> Day
    day = 14
    name = Pipes
    description =
        Hey
    images =
        |> Image
            img/day_14.png

|> Day
    day = 15
    name = Pattern
    description =
        Hey
    images =
        |> Image
            img/day_15_1887.png
        |> Image
            img/day_15_1538.png
        |> Image
            img/day_15_3109.png

|> Day
    day = 16
    name = Fave
    description =
        Hey
    images =
        |> Image
            img/day_16_5.png
        |> Image
            img/day_16_2255.png
        |> Image
            img/day_16_5699.png
        |> Image
            img/day_16_8385.png

|> Day
    day = 17
    name = Sheaf
    description =
        Hey
    images =
        |> Image
            img/day_17.mov

|> Day
    day = 18
    name = Rays
    description =
        Hey
    images =
        |> Image
            img/day_18.png

|> Day
    day = 19
    name = Bar
    description =
        Hey
    images =
        |> Image
            img/day_19.png

|> Day
    day = 20
    name = Dashes
    description =
        Hey
    images =
        |> Image
            img/day_20.png

|> Day
    day = 21
    name = Carpet
    description =
        Hey
    images =
        |> Image
            img/day_21.png

|> Day
    day = 22
    name = Triangulation
    description =
        Hey
    images =
        |> Image
            img/day_22.png

|> Day
    day = 23
    name = Glass
    description =
        Hey
    images =
        |> Image
            img/day_23.png

|> Day
    day = 24
    name = Mountains
    description =
        Hey
    images =
        |> Image
            img/day_24.png

|> Day
    day = 25
    name = Cubes
    description =
        Hey
    images =
        |> Image
            img/day_25.png

|> Day
    day = 26
    name = Packing
    description =
        Hey
    images =
        |> Image
            img/day_26.png

|> Day
    day = 27
    name = Blocks
    description =
        Hey
    images =
        |> Image
            img/day_27.png

|> Day
    day = 28
    name = Glitch
    description =
        Hey
    images =
        |> Image
            img/day_28.png

|> Day
    day = 29
    name = Polygon Lines
    description =
        Hey
    images =
        |> Image
            img/day_29.png

|> Day
    day = 30
    name = Bye
    description =
        Hey
    images =
        |> Image
            img/day_30.png

"""
